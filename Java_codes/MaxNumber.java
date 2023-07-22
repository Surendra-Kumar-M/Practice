import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;


public class MaxNumber extends HttpServlet
{
protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException,IOException{
res.setContentType("text/html");
PrintWriter out=res.getWriter();

int a=Integer.parseInt(req.getParameter("Number1"));
int b=Integer.parseInt(req.getParameter("Number2"));

if(a>b)
out.println("<h4>The Maximum Number is: "+a+"</h4>");
else
out.println("<h4>The Maximum Number is: "+a+"</h4>");

}
}