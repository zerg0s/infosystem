package informationsystem.loggerWindow.hyperlink;

import javafx.geometry.VPos;
import org.fxmisc.richtext.GenericStyledArea;
import org.fxmisc.richtext.TextExt;
import org.fxmisc.richtext.model.ReadOnlyStyledDocument;
import org.fxmisc.richtext.model.SegmentOps;
import org.fxmisc.richtext.model.StyledDocument;
import org.fxmisc.richtext.model.TextOps;
import org.reactfx.util.Either;

import java.awt.*;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.List;
import java.util.Optional;
import java.util.function.Consumer;

public class TextHyperlinkArea extends GenericStyledArea<Void, Either<String, Hyperlink>, RichTextStyle> {

    private static final TextOps<String, RichTextStyle> STYLED_TEXT_OPS = SegmentOps.styledTextOps();
    private static final HyperlinkOps<RichTextStyle> HYPERLINK_OPS = new HyperlinkOps<>();

    private static final TextOps<Either<String, Hyperlink>, RichTextStyle> EITHER_OPS = STYLED_TEXT_OPS._or(HYPERLINK_OPS, (s1, s2) -> Optional.empty());

    private static Consumer<String> showLink = (string) -> {
        try
        {
            Desktop.getDesktop().browse(new URI(string));
        }
        catch (IOException | URISyntaxException e)
        {
            throw new RuntimeException(e);
        }
    };

    public TextHyperlinkArea() {
        this(showLink);
    }

    public TextHyperlinkArea(Consumer<String> showLink) {
        super(
                null,
                (t, p) -> {},
                RichTextStyle.EMPTY,
                EITHER_OPS,
                e -> e.getSegment().unify(
                        text ->
                            createStyledTextNode(t -> {
                                t.setText(text);
                                t.setStyle(e.getStyle().toCss());
                        }),
                        hyperlink ->
                            createStyledTextNode(t -> {
                                if (hyperlink.isReal()) {
                                    t.setText(hyperlink.getDisplayedText());
                                    t.getStyleClass().add("hyperlink");
                                    t.setOnMouseClicked(ae -> showLink.accept(hyperlink.getLink()));
                                }
                        })
                )
        );

        getStyleClass().add("text-hyperlink-area");
        getStylesheets().add(getClass().getResource("/informationsystem/loggerWindow/hyperlink/text-hyperlink-area.css").toExternalForm());
    }

    public void appendWithLink(String displayedText, String link) {
        replaceWithLink(getLength(), getLength(), displayedText, link);
    }

    public void replaceWithLink(int start, int end, String displayedText, String link) {
        replace(start, end, ReadOnlyStyledDocument.fromSegment(
                Either.right(new Hyperlink(displayedText, displayedText, link)),
                null,
                RichTextStyle.EMPTY,
                EITHER_OPS
        ));
    }

    @Override
    public void replaceText(int start, int end, String text) {
        
        if (start > 0 && end > 0) {
            int s = Math.max(0, start-1);
            int e = Math.min(end+1, getLength()-1);
            List<Either<String, Hyperlink>> segList = getDocument().subSequence( s, e ).getParagraph(0).getSegments();
            if (!segList.isEmpty() && segList.get(0).isRight()) {
                String link = segList.get(0).getRight().getLink();
                replaceWithLink( start, end, text, link );
                return;
            }
        }
        StyledDocument<Void, Either<String, Hyperlink>, RichTextStyle> doc = ReadOnlyStyledDocument.fromString(
            text, getParagraphStyleForInsertionAt(start), getTextStyleForInsertionAt(start), EITHER_OPS
        );
        replace(start, end, doc);
    }

    public static TextExt createStyledTextNode(Consumer<TextExt> applySegment) {
        TextExt t = new TextExt();
        t.setTextOrigin(VPos.TOP);
        applySegment.accept(t);
        return t;
    }
}
