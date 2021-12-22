package informationsystem.loggerWindow;

import informationsystem.loggerWindow.hyperlink.HyperlinkDemo;
import informationsystem.loggerWindow.hyperlink.RichTextStyle;
import informationsystem.loggerWindow.hyperlink.TextHyperlinkArea;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import org.fxmisc.flowless.VirtualizedScrollPane;
import org.reactfx.util.Either;
import tools.PvkLogger;

import java.net.URL;
import java.util.ResourceBundle;

public class LoggerWindowController implements Initializable {
    @FXML
    private Button btnClose;
    @FXML
    private BorderPane borderPaneMain;

    private PvkLogger logger;
    private Stage stage;
    private TextHyperlinkArea area;
    private VirtualizedScrollPane<TextHyperlinkArea> vsPane;

    @FXML
    public void appendLogs(String text) {
        appendLogsLn(text, RichTextStyle.bold(false).updateTextColor(Color.BLACK));
    }

    public void appendLogsError(String text) {
        appendLogString(text, RichTextStyle.bold(false).updateTextColor(Color.RED));
    }

    public void appendLogsBold(String text) {
        appendLogString(text, RichTextStyle.bold(true).updateTextColor(Color.BLACK));
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
        area =  new TextHyperlinkArea();
        vsPane = new VirtualizedScrollPane<>(area, ScrollPane.ScrollBarPolicy.AS_NEEDED, ScrollPane.ScrollBarPolicy.AS_NEEDED);
        borderPaneMain.setCenter(vsPane);
    }

    public Stage getStage() {
        return stage;
    }

    public void setStage(Stage stage) {
        this.stage = stage;
    }

    private void appendLogsLn(String text, RichTextStyle style) {
        appendLogString(text, style);
        appendText("\n");
    }

    private void appendText(String text) {
        Platform.runLater(() -> {
            area.appendText(text);
        });
        scrollToTheEnd();
    }

    private void appendLogString(String text, RichTextStyle style) {
        Platform.runLater(() -> {
            area.append(Either.left(text), style);
        });
        scrollToTheEnd();
    }

    private void scrollToTheEnd() {
        Platform.runLater(() -> {
            if (area.totalHeightEstimateProperty().getValue() != null) {
                area.scrollYBy(area.totalHeightEstimateProperty().getValue());
            }
        });
    }
}
