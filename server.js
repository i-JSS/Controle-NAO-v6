const http = require('http');
const fs = require('fs');
const path = require('path');

let controleState = {};

const PORT = 8090;

const server = http.createServer((req, res) => {
    if (req.method === 'GET') {
        if (req.url === '/controle') {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(controleState));
        } else {

            let filePath = path.join(__dirname, req.url === '/' ? 'index.html' : req.url);
            let ext = path.extname(filePath);
            let contentType = {
                '.html': 'text/html',
                '.js': 'text/javascript',
                '.css': 'text/css'
            }[ext] || 'application/octet-stream';

            fs.readFile(filePath, (err, content) => {
                if (err) {
                    res.writeHead(404);
                    res.end('Arquivo não encontrado');
                } else {
                    res.writeHead(200, { 'Content-Type': contentType });
                    res.end(content);
                }
            });
        }
    } else if (req.method === 'POST' && req.url === '/controle') {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', () => {
            try {
                controleState = JSON.parse(body);
                console.log("Botão atual:", controleState.id || "(nenhum)");
            } catch (e) {
                controleState = {};
                console.log("Erro ao ler controle:", e.message);
            }
            res.writeHead(200);
            res.end();
        });
    } else {
        res.writeHead(405);
        res.end('Método não permitido');
    }
});

server.listen(PORT, '0.0.0.0', () => {
    const os = require('os');
    const interfaces = os.networkInterfaces();
    console.log(`Servidor rodando em:`);

    for (let name in interfaces) {
        for (let iface of interfaces[name]) {
            if (iface.family === 'IPv4' && !iface.internal) {
                console.log(`http://${iface.address}:${PORT}`);
            }
        }
    }
});
