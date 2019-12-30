var index = document.getElementById("index")
var p = document.getElementById("p")
index.addEventListener("keypress", function(){
  if(event.keyCode == 13)
  {
    var URL = "/data/graph_" + index.value + ".txt";
    p.innerHTML = "Block Index: " + index.value;
    $.ajax({
      url: URL,
      success: function (data, status) {
    
        let text;
        let edges = [];
        let G = new jsnx.MultiDiGraph;
    
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
        element: '#all', 
        withLabels: false, 
        nodeStyle: {
            fill: function(d) { 
                return d.data.color; 
            },
        }, 
        nodeAttr: {
          r: 2,
        },
        labelStyle: {
          fill: 'white',
        },
        // edge_style: { 
        //   'stroke-width': 0.1
        // },
        with_edge_labels: true,
        stickyDrag: true,
        with: 1000,
        height: 1000
        });
      },
      error: function (data, status) {
        console.log(arguments);
      }
    });
  }
})

