package informationsystem.xml;

import javafx.util.Pair;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class OnlineXmlReader extends XmlReader {
    public static List<String> getDescription(String readXml, String descriptionTag, String itemTag) throws IOException, SAXException, ParserConfigurationException {
        NodeList nodes = loadXMLFromString(readXml).getDocumentElement()
                .getElementsByTagName(itemTag);
        List<String> nodesList = new ArrayList<>();
        for (int i = 0; i < nodes.getLength(); i++) {
            nodesList.add(((Node) nodes.item(i)).getChildNodes().item(0).getNodeValue());
        }
        return nodesList;
    }

    public static Pair<String, String> getFilePath(String xml, String attribute) {
        Pair<String, String> fromTo = new Pair<String, String>("", "");
        try {
            final Document doc = loadXMLFromString(xml);
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();

            //xpath for settings paths
            String xPath = String.format(".//files/file[@descr=\"%s\"]", attribute);
            XPathExpression exprFrom = xpath.compile(xPath);
            Element fileNode = (Element) exprFrom.evaluate(doc, XPathConstants.NODE);
            fromTo = new Pair<String, String>(fileNode.getAttribute("from"),
                    fileNode.getAttribute("to"));
        } catch (ParserConfigurationException | IOException | SAXException | XPathExpressionException e) {
            e.printStackTrace();
        }
        return fromTo;
    }

    public static ArrayList<Pair<String, String>> getAllAdditionalFiles(String xml) {
        Pair<String, String> fromTo;
        ArrayList<Pair<String, String>> files = new ArrayList<>();
        try {
            final Document doc = loadXMLFromString(xml);
            NodeList fileNodes = ((Element) doc.getElementsByTagName("root").item(0)).getElementsByTagName("file");
            for (int i = 0; i < fileNodes.getLength(); i++) {
                Element fileElement = (Element) fileNodes.item(i);
                fromTo = new Pair<String, String>(fileElement.getAttribute("from"),
                        fileElement.getAttribute("to"));
                files.add(fromTo);
            }
        } catch (ParserConfigurationException | IOException | SAXException e) {
            e.printStackTrace();
        }
        return files;
    }
}
