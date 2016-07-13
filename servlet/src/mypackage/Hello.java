package mypackage;

import java.io.*;
import javax.servlet.*;

public class Hello extends GenericServlet {
  public void service(final ServletRequest request, final ServletResponse response)
  throws ServletException, IOException {
    response.setContentType("text/html");
    final PrintWriter pw = response.getWriter();
    try {
      pw.println("<p>Hello, Servlet!</p>");
    } finally {
      pw.close();
    }
  }
}

