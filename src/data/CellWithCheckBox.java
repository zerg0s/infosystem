package data;

import javafx.beans.property.BooleanProperty;
import javafx.beans.property.SimpleBooleanProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class CellWithCheckBox {
    private final StringProperty title = new SimpleStringProperty();
    private final BooleanProperty completed = new SimpleBooleanProperty();

    public CellWithCheckBox(String title, boolean completed) {
        setTitle(title);
        setCompleted(completed);
    }

    public final StringProperty titleProperty() {
        return this.title;
    }


    public final String getTitle() {
        return this.titleProperty().get();
    }


    public final void setTitle(final String title) {
        this.titleProperty().set(title);
    }


    public final BooleanProperty completedProperty() {
        return this.completed;
    }


    public final boolean isCompleted() {
        return this.completedProperty().get();
    }


    public final void setCompleted(final boolean completed) {
        this.completedProperty().set(completed);
    }
}
