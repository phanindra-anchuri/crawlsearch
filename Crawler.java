package crawler;

import java.io.IOException;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Crawler {

  private String baseUrl;

  private int crawlDepth;

  public static void main(String[] args) throws IOException {
    Crawler crawler = new Crawler();
    crawler.baseUrl = "http://www.google.com";
    crawler.crawlDepth = 2;
    crawler.crawl();
  }

  public List<String> extractLinks(String url) throws IOException {
    List<String> urls = new ArrayList<String>();
    Document doc = Jsoup.connect(url).get();
    Elements links = doc.select("a[href]");
    for (Element link : links) {
      System.out.println(link.attr("abs:href"));
      urls.add(link.attr("abs:href"));
    }
    return urls;
  }

  public void crawl() throws IOException {
    int depth = 0;
    Deque<String> queue = new ArrayDeque<String>();
    queue.add(baseUrl);
    while(!queue.isEmpty() && depth <= crawlDepth) {
      System.out.println("Depth "+ depth);
      String url = queue.removeFirst();
      List<String> urls = extractLinks(url);
      depth++;
      queue.addAll(urls);
    }
  }
}
