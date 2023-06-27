const app = require('express')(),
  server = require('http').Server(app),
  io = require('socket.io')(server),
  rtsp = require('rtsp-ffmpeg');
server.listen(3580); //열고 싶은 포트번호 입력
var uri = 'rtsp://admin:cosmotier1!@192.168.0.64:554/ISAPI/streaming/channels/101', // 하이크비전 
  stream = new rtsp.FFMpeg({input: uri});
io.on('connection', function(socket) {
  var pipeStream = function(data) {
    socket.emit('data', data.toString('base64'));
  };
  stream.on('data', pipeStream);
  socket.on('disconnect', function() {
    stream.removeListener('data', pipeStream);
  });
});
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});