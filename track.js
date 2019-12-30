$.ajax({
  url: "graph_100.txt",
  success: function (data, status) {

    let text;
    let a = [];
    let edges = [];
    let G = new jsnx.DiGraph();

    console.log(arguments);
    text = data.split("\n");
    let iedge;
    for(let i = 0; i < text.length; i++){
      let w = text[i].split(" ");
      edges.push([Number(w[0]), Number(w[1]), Number(w[2])]);
    }
    console.log(iedge)
    G.addEdgesFrom(edges);
    jsnx.draw(G, {
    element: '#track', 
    withLabels: false, 
    nodeStyle: {
        fill: function(d) { 
            return d.data.color; 
        }
    }, 
    labelStyle: {fill: 'white'},
    stickyDrag: true,
    with: 1000,
    height: 500
    });

  },
  error: function (data, status) {
    console.log(arguments);
  }
});
