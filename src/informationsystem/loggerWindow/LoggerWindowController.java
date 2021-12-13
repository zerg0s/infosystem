package informationsystem.loggerWindow;

import informationsystem.loggerWindow.hyperlink.Hyperlink;
import informationsystem.loggerWindow.hyperlink.RichTextStyle;
import informationsystem.loggerWindow.hyperlink.TextHyperlinkArea;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.scene.text.TextFlow;
import javafx.stage.Stage;
import org.fxmisc.flowless.VirtualizedScrollPane;
import org.fxmisc.richtext.InlineCssTextArea;
import org.fxmisc.richtext.StyledTextArea;
import org.fxmisc.richtext.TextExt;
import org.fxmisc.richtext.model.StyledDocument;
import org.fxmisc.richtext.model.Paragraph;
import org.reactfx.util.Either;
import tools.PvkLogger;

import java.net.URL;
import java.time.format.TextStyle;
import java.util.ResourceBundle;

public class LoggerWindowController implements Initializable {
    @FXML
    private Button btnClose;
    @FXML
    private ScrollPane scrollPaneMain;

    private PvkLogger logger;
    private Stage stage;
    private TextHyperlinkArea area = new TextHyperlinkArea();

    @FXML
    public void appendLogs(String text) {
        appendLogsLn(text, RichTextStyle.bold(false).updateTextColor(Color.BLACK));
    }

    public void appendLogsError(String text) {
        appendLogsLn(text, RichTextStyle.bold(false).updateTextColor(Color.RED));
    }

    public void appendLogsBold(String text) {
        appendLogs(text, RichTextStyle.bold(true).updateTextColor(Color.BLACK));
    }

    public void appendLogsBoldLn(String text) {
        appendLogsLn(text, RichTextStyle.bold(true).updateTextColor(Color.BLACK));
    }

    public void appendHyperLink(String text, String url) {
        Platform.runLater(() -> {
            area.appendWithLink(text, url);
        });
    }

    public void setLogger(PvkLogger logger) {
        this.logger = logger;
    }

    @FXML
    public void shutdown() {
        // get a handle to the stage
        Stage stage = (Stage) btnClose.getScene().getWindow();
        // do what you have to do
        stage.close();
    }


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        area.setWrapText(true);
        scrollPaneMain.setFitToHeight(true);
        scrollPaneMain.setFitToWidth(true);
        VirtualizedScrollPane<TextHyperlinkArea> vsPane = new VirtualizedScrollPane<>(area);
        scrollPaneMain.setContent(vsPane);
    }

    public Stage getStage() {
        return stage;
    }

    public void setStage(Stage stage) {
        this.stage = stage;
    }

    private void appendLogsLn(String text, RichTextStyle style) {
        String finalText = text + "\n";
        Platform.runLater(() -> {
            area.append(Either.left(finalText), style);
        });
    }
    private void appendLogs(String text, RichTextStyle style) {
        String finalText = text;
        Platform.runLater(() -> {
            area.append(Either.left(finalText), style);
        });
    }
}
