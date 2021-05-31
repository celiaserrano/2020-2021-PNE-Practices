import http.server
import socketserver
import termcolor

from urllib.parse import urlparse, parse_qs
import functions as fu
import funct_gene

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)


        error = False
        context = {}
        if path_name == "/":

            contents = fu.read_template_html_file("./html/index.html").render(context=context)

        elif path_name == "/listSpecies":
            if len(arguments) == 0:
                contents = fu.limit_species()
            elif len(arguments) == 1:
                try:
                    limits = int(arguments["limit"][0])
                    contents = fu.limit_species(limits)
                except (KeyError, ValueError):
                    error = True
            else:
                error = True


        elif path_name == "/karyotype":
            specie = arguments["specie"][0]
            contents = fu.print_karyotype(specie)

        elif path_name == "/chromosomeLength":
            specie = arguments["specie"][0]
            chromo = arguments["chromo"][0]
            contents = fu.print_lenght(specie, chromo)

        elif path_name == "/geneSeq":
            gene = arguments["gene"][0]
            contents = funct_gene.open_seq(gene)

        elif path_name == "/geneInfo":
            gene = arguments["gene"][0]
            contents = funct_gene.info_seq(gene)

        elif path_name == "/geneCalc":
            gene = arguments["gene"][0]
            contents = funct_gene.calc_seq(gene)


        else:
            contents = fu.read_template_html_file("./html/error.html").render()


        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())


        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
