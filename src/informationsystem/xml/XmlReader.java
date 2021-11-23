/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem.xml;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.logging.Logger;
import javax.xml.namespace.QName;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import informationsystem.FXMLDocumentController;
import org.w3c.dom.*;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

/**
 * @author Zerg0s
 */
public class XmlReader {

    private XPathFactory xPathfactory;
    protected XPath xpath;
    protected Document doc;
    protected String filePath = "";

    public XmlReader(String pathToXml) {
        this();
        this.filePath = pathToXml;
        doc = getDocument(filePath);
    }

    public XmlReader() {
        xPathfactory = XPathFactory.newInstance();
        xpath = xPathfactory.newXPath();
    }
    public String getTestFolderBySubject(String subjectFromIssue) {
        String testFolderPathInXml = "";
        try {
            //xpath for getting names
            XPathExpression subjectFromXml = xpath.compile(".//test");
            NodeList listOfTestNodes = (NodeList) subjectFromXml.evaluate(doc, XPathConstants.NODESET);

            //тут можно добавить более "умный" поиск, пока ищем только - полное совпадение
            for (int i = 0; i < listOfTestNodes.getLength(); i++) {
                Element e = (Element) listOfTestNodes.item(i);
                if (subjectFromIssue.toLowerCase().contains(e.getAttribute("subject").toLowerCase())) {
                    testFolderPathInXml = e.getAttribute("testSetFolder");
                }
            }
        } catch (XPathExpressionException ex) {
            logger.info(ex.getMessage());
        }
        return testFolderPathInXml;
    }

   /// private methods
   protected Object xPathEvaluate(Element rootNode, String xPathStringElem, XPath xpath, QName node) {
        try {
            return xpath.evaluate(xPathStringElem, rootNode, node);
        } catch (XPathExpressionException e) {
            logger.info(e.getMessage());
        }
        return null;
    }

    protected Document getDocument(String filePath) {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setIgnoringElementContentWhitespace(true);
        DocumentBuilder builder = null;
        try {
            builder = factory.newDocumentBuilder();
            return builder.parse(filePath);
        } catch (SAXException | IOException | ParserConfigurationException e) {
            e.printStackTrace();
        }
        return null;
    }

    protected void saveXml(Document doc, String filePath) throws TransformerException {
        Transformer transformer = TransformerFactory.newInstance().newTransformer();
        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new File(filePath));
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");
        transformer.transform(source, result);
        //Crunch to remove empty lines
        try {
            List<String> xmlString = Files.readAllLines(Path.of(filePath));
            Files.delete(Path.of(filePath));
            BufferedWriter wr = new BufferedWriter(new FileWriter(filePath, StandardCharsets.UTF_8));
            for (String s : xmlString) {
                if (!s.trim().isEmpty()) {
                    wr.write(s);
                    wr.newLine();
                }
            }
            wr.flush();
            wr.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

   //// Static methods
    public static String getValue(String tag, Element element) {
        if (tag != null && element != null) {
            Node node = element.getElementsByTagName(tag).item(0);
            if (node != null) {
                Node childNode = node.getChildNodes().item(0);
                return childNode.getNodeValue();
            }
        }
        return "";
    }

    public static Document loadXMLFromString(String xml) throws ParserConfigurationException, IOException, SAXException {
        DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
        InputSource is = new InputSource(new StringReader(xml));
        return builder.parse(is);
    }

    public static String getTextTagValue(String tag, Document doc) {
        return getValue(tag, doc.getDocumentElement());
    }

    protected static Logger logger = Logger.getLogger(FXMLDocumentController.class.getSimpleName());
}
