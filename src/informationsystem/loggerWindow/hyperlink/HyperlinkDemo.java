package informationsystem.loggerWindow.hyperlink;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import org.fxmisc.flowless.VirtualizedScrollPane;

import java.awt.*;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.function.Consumer;

public class HyperlinkDemo extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        Consumer<String> showLink = (string) -> {
            try {
                Desktop.getDesktop().browse(new URI(string));
            } catch (IOException | URISyntaxException e) {
                throw new RuntimeException(e);
            }
        };
        TextHyperlinkArea area = new TextHyperlinkArea(showLink);

        area.appendText("Some text in the area\n");
        area.appendWithLink("Google.com", "http://www.google.com");

        VirtualizedScrollPane<TextHyperlinkArea> vsPane = new VirtualizedScrollPane<>(area);

        Scene scene = new Scene(vsPane, 500, 500);
        primaryStage.setScene(scene);
        primaryStage.show();
        for (int i = 0; i < 1000; i++) {
            area.appendText("AAAAAA\n");
        }
        area.scrollYBy(area.getTotalHeightEstimate());
    }
}
