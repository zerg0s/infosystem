package informationsystem.loggerWindow.hyperlink;

import javafx.scene.paint.Color;
import org.fxmisc.richtext.model.Codec;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.nio.charset.MalformedInputException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 * Holds information about the style of a text fragment.
 */
public class RichTextStyle {

    public static final RichTextStyle EMPTY = new RichTextStyle();

    public static final Codec<RichTextStyle> CODEC = new Codec<RichTextStyle>() {

        private final Codec<Optional<String>> OPT_STRING_CODEC =
                Codec.optionalCodec(Codec.STRING_CODEC);
        private final Codec<Optional<Color>> OPT_COLOR_CODEC =
                Codec.optionalCodec(Codec.COLOR_CODEC);

        @Override
        public String getName() {
            return "text-style";
        }

        @Override
        public void encode(DataOutputStream os, RichTextStyle s)
                throws IOException {
            os.writeByte(encodeBoldItalicUnderlineStrikethrough(s));
            os.writeInt(encodeOptionalUint(s.fontSize));
            OPT_STRING_CODEC.encode(os, s.fontFamily);
            OPT_COLOR_CODEC.encode(os, s.textColor);
            OPT_COLOR_CODEC.encode(os, s.backgroundColor);
        }

        @Override
        public RichTextStyle decode(DataInputStream is) throws IOException {
            byte bius = is.readByte();
            Optional<Integer> fontSize = decodeOptionalUint(is.readInt());
            Optional<String> fontFamily = OPT_STRING_CODEC.decode(is);
            Optional<Color> textColor = OPT_COLOR_CODEC.decode(is);
            Optional<Color> bgrColor = OPT_COLOR_CODEC.decode(is);
            return new RichTextStyle(
                    bold(bius), italic(bius), underline(bius), strikethrough(bius),
                    fontSize, fontFamily, textColor, bgrColor);
        }

        private int encodeBoldItalicUnderlineStrikethrough(RichTextStyle s) {
            return encodeOptionalBoolean(s.bold) << 6 |
                   encodeOptionalBoolean(s.italic) << 4 |
                   encodeOptionalBoolean(s.underline) << 2 |
                   encodeOptionalBoolean(s.strikethrough);
        }

        private Optional<Boolean> bold(byte bius) throws IOException {
            return decodeOptionalBoolean((bius >> 6) & 3);
        }

        private Optional<Boolean> italic(byte bius) throws IOException {
            return decodeOptionalBoolean((bius >> 4) & 3);
        }

        private Optional<Boolean> underline(byte bius) throws IOException {
            return decodeOptionalBoolean((bius >> 2) & 3);
        }

        private Optional<Boolean> strikethrough(byte bius) throws IOException {
            return decodeOptionalBoolean((bius >> 0) & 3);
        }

        private int encodeOptionalBoolean(Optional<Boolean> ob) {
            return ob.map(b -> 2 + (b ? 1 : 0)).orElse(0);
        }

        private Optional<Boolean> decodeOptionalBoolean(int i) throws IOException {
            switch(i) {
                case 0: return Optional.empty();
                case 2: return Optional.of(false);
                case 3: return Optional.of(true);
            }
            throw new MalformedInputException(0);
        }

        private int encodeOptionalUint(Optional<Integer> oi) {
            return oi.orElse(-1);
        }

        private Optional<Integer> decodeOptionalUint(int i) {
            return (i < 0) ? Optional.empty() : Optional.of(i);
        }
    };

    public static RichTextStyle bold(boolean bold) { return EMPTY.updateBold(bold); }
    public static RichTextStyle italic(boolean italic) { return EMPTY.updateItalic(italic); }
    public static RichTextStyle underline(boolean underline) { return EMPTY.updateUnderline(underline); }
    public static RichTextStyle strikethrough(boolean strikethrough) { return EMPTY.updateStrikethrough(strikethrough); }
    public static RichTextStyle fontSize(int fontSize) { return EMPTY.updateFontSize(fontSize); }
    public static RichTextStyle fontFamily(String family) { return EMPTY.updateFontFamily(family); }
    public static RichTextStyle textColor(Color color) { return EMPTY.updateTextColor(color); }
    public static RichTextStyle backgroundColor(Color color) { return EMPTY.updateBackgroundColor(color); }

    static String cssColor(Color color) {
        int red = (int) (color.getRed() * 255);
        int green = (int) (color.getGreen() * 255);
        int blue = (int) (color.getBlue() * 255);
        return "rgb(" + red + ", " + green + ", " + blue + ")";
    }

    final Optional<Boolean> bold;
    final Optional<Boolean> italic;
    final Optional<Boolean> underline;
    final Optional<Boolean> strikethrough;
    final Optional<Integer> fontSize;
    final Optional<String> fontFamily;
    final Optional<Color> textColor;
    final Optional<Color> backgroundColor;

    public RichTextStyle() {
        this(
            Optional.empty(),
            Optional.empty(),
            Optional.empty(),
            Optional.empty(),
            Optional.empty(),
            Optional.empty(),
            Optional.empty(),
            Optional.empty()
        );
    }

    public RichTextStyle(
            Optional<Boolean> bold,
            Optional<Boolean> italic,
            Optional<Boolean> underline,
            Optional<Boolean> strikethrough,
            Optional<Integer> fontSize,
            Optional<String> fontFamily,
            Optional<Color> textColor,
            Optional<Color> backgroundColor) {
        this.bold = bold;
        this.italic = italic;
        this.underline = underline;
        this.strikethrough = strikethrough;
        this.fontSize = fontSize;
        this.fontFamily = fontFamily;
        this.textColor = textColor;
        this.backgroundColor = backgroundColor;
    }

    @Override
    public int hashCode() {
        return Objects.hash(
                bold, italic, underline, strikethrough,
                fontSize, fontFamily, textColor, backgroundColor);
    }

    @Override
    public boolean equals(Object other) {
        if(other instanceof RichTextStyle) {
            RichTextStyle that = (RichTextStyle) other;
            return Objects.equals(this.bold,            that.bold) &&
                   Objects.equals(this.italic,          that.italic) &&
                   Objects.equals(this.underline,       that.underline) &&
                   Objects.equals(this.strikethrough,   that.strikethrough) &&
                   Objects.equals(this.fontSize,        that.fontSize) &&
                   Objects.equals(this.fontFamily,      that.fontFamily) &&
                   Objects.equals(this.textColor,       that.textColor) &&
                   Objects.equals(this.backgroundColor, that.backgroundColor);
        } else {
            return false;
        }
    }

    @Override
    public String toString() {
        List<String> styles = new ArrayList<>();

        bold           .ifPresent(b -> styles.add(b.toString()));
        italic         .ifPresent(i -> styles.add(i.toString()));
        underline      .ifPresent(u -> styles.add(u.toString()));
        strikethrough  .ifPresent(s -> styles.add(s.toString()));
        fontSize       .ifPresent(s -> styles.add(s.toString()));
        fontFamily     .ifPresent(f -> styles.add(f.toString()));
        textColor      .ifPresent(c -> styles.add(c.toString()));
        backgroundColor.ifPresent(b -> styles.add(b.toString()));

        return String.join(",", styles);
    }

    public String toCss() {
        StringBuilder sb = new StringBuilder();

        if(bold.isPresent()) {
            if(bold.get()) {
                sb.append("-fx-font-weight: bold;");
            } else {
                sb.append("-fx-font-weight: normal;");
            }
        }

        if(italic.isPresent()) {
            if(italic.get()) {
                sb.append("-fx-font-style: italic;");
            } else {
                sb.append("-fx-font-style: normal;");
            }
        }

        if(underline.isPresent()) {
            if(underline.get()) {
                sb.append("-fx-underline: true;");
            } else {
                sb.append("-fx-underline: false;");
            }
        }

        if(strikethrough.isPresent()) {
            if(strikethrough.get()) {
                sb.append("-fx-strikethrough: true;");
            } else {
                sb.append("-fx-strikethrough: false;");
            }
        }

        if(fontSize.isPresent()) {
            sb.append("-fx-font-size: " + fontSize.get() + "pt;");
        }

        if(fontFamily.isPresent()) {
            sb.append("-fx-font-family: " + fontFamily.get() + ";");
        }

        if(textColor.isPresent()) {
            Color color = textColor.get();
            sb.append("-fx-fill: " + cssColor(color) + ";");
        }

        if(backgroundColor.isPresent()) {
            Color color = backgroundColor.get();
            sb.append("-rtfx-background-color: " + cssColor(color) + ";");
        }

        return sb.toString();
    }

    public RichTextStyle updateWith(RichTextStyle mixin) {
        return new RichTextStyle(
                mixin.bold.isPresent() ? mixin.bold : bold,
                mixin.italic.isPresent() ? mixin.italic : italic,
                mixin.underline.isPresent() ? mixin.underline : underline,
                mixin.strikethrough.isPresent() ? mixin.strikethrough : strikethrough,
                mixin.fontSize.isPresent() ? mixin.fontSize : fontSize,
                mixin.fontFamily.isPresent() ? mixin.fontFamily : fontFamily,
                mixin.textColor.isPresent() ? mixin.textColor : textColor,
                mixin.backgroundColor.isPresent() ? mixin.backgroundColor : backgroundColor);
    }

    public RichTextStyle updateBold(boolean bold) {
        return new RichTextStyle(Optional.of(bold), italic, underline, strikethrough, fontSize, fontFamily, textColor, backgroundColor);
    }

    public RichTextStyle updateItalic(boolean italic) {
        return new RichTextStyle(bold, Optional.of(italic), underline, strikethrough, fontSize, fontFamily, textColor, backgroundColor);
    }

    public RichTextStyle updateUnderline(boolean underline) {
        return new RichTextStyle(bold, italic, Optional.of(underline), strikethrough, fontSize, fontFamily, textColor, backgroundColor);
    }

    public RichTextStyle updateStrikethrough(boolean strikethrough) {
        return new RichTextStyle(bold, italic, underline, Optional.of(strikethrough), fontSize, fontFamily, textColor, backgroundColor);
    }

    public RichTextStyle updateFontSize(int fontSize) {
        return new RichTextStyle(bold, italic, underline, strikethrough, Optional.of(fontSize), fontFamily, textColor, backgroundColor);
    }

    public RichTextStyle updateFontFamily(String fontFamily) {
        return new RichTextStyle(bold, italic, underline, strikethrough, fontSize, Optional.of(fontFamily), textColor, backgroundColor);
    }

    public RichTextStyle updateTextColor(Color textColor) {
        return new RichTextStyle(bold, italic, underline, strikethrough, fontSize, fontFamily, Optional.of(textColor), backgroundColor);
    }

    public RichTextStyle updateBackgroundColor(Color backgroundColor) {
        return new RichTextStyle(bold, italic, underline, strikethrough, fontSize, fontFamily, textColor, Optional.of(backgroundColor));
    }
}