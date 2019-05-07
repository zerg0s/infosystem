/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import java.util.Random;

/**
 *
 * @author Politsyn
 */
public class PhrasesGenerator {

    private String[] phraseStorage
            = {"Great work!", "Awesome! 10 out of 10!",
                "Nice attempt.", "Code accepted.",
                "Your know PEP8. You can talk to Robot.",
                "My god, one of the best styles.", "Stylish code. Accepted",
                "Outstanding. Not many can PEP so easily.", "Gj! See u later!",
                "How do you do, Mr. Know-all?", "It\'s really worth to respect."};

    public String getSuccessRandomPhrase() {
        int i = new Random().nextInt(100);
        return phraseStorage[i % phraseStorage.length];
    }
}
