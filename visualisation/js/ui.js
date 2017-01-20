function bin2String(array) {
  var result = "";
  for (var i = 0; i < array.length; i++) {
    result += String.fromCharCode(array[i]);
  }
  return result;
}

window.onload = function () {

    var pyr = [0, 0, 0];

    var client = mqtt.connect("ws://127.0.0.1:9001") // you add a ws:// url here
    client.subscribe("orientation")

    client.on("message", function (topic, payload) {
        payload = bin2String(payload);

        var pyr_temp = payload.split(":");

        pyr[0] = (parseFloat(pyr_temp[0]) + 180)  * (Math.PI / 180);
        pyr[1] = (parseFloat(pyr_temp[1]) + 180)  * (Math.PI / 180);
        pyr[2] = (parseFloat(pyr_temp[2]) + 180)  * (Math.PI / 180);

        //console.log(pyr);
    })

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 1, 10000);
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    var geometry = new THREE.BoxGeometry(700, 700, 700, 10, 10, 10);
    var material = new THREE.MeshBasicMaterial({color: 0xfffff, wireframe: true});
    var cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    camera.position.z = 1000;
    function render() {
        requestAnimationFrame(render);

        var ux = new THREE.Vector3(1,0,0);
        var uy = new THREE.Vector3(0,1,0);
        var uz = new THREE.Vector3(0,0,1);


        cube.rotation.x = pyr[0];
        cube.rotation.y = pyr[1];
        cube.rotation.z = pyr[2];
        renderer.render(scene, camera);
    };
    render();

}
