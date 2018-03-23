﻿var toolbar, symbol, geomTask;
require([
  "esri/map",
  "esri/toolbars/draw",
  "esri/graphic",
  "esri/layers/ArcGISDynamicMapServiceLayer",
  "esri/symbols/SimpleMarkerSymbol",
  "esri/symbols/SimpleLineSymbol",
  "esri/symbols/SimpleFillSymbol",

  "dojo/parser", "dijit/registry",

  "dijit/layout/BorderContainer", "dijit/layout/ContentPane",
  "dijit/form/Button", "dijit/WidgetSet", "dojo/domReady!"
], function (
  Map, Draw, Graphic, ArcGISDynamicMapServiceLayer,
  SimpleMarkerSymbol, SimpleLineSymbol, SimpleFillSymbol,
  parser, registry
) {
    parser.parse();

    // loop through all dijits, connect onClick event
    // listeners for buttons to activate drawing tools
    var al = document.getElementById("drawplota");
    al.onclick = function (e) {
        createToolbar(map);
        activateTool();
    }

    function activateTool() {
        toolbar.activate(Draw["FREEHAND_POLYGON"]);
        map.hideZoomSlider();
    }

    function createToolbar(map) {
        toolbar = new Draw(map);
        toolbar.on("draw-end", addToMap);
    }


    //infoWindow中保存按钮的事件
    function savegraphic(index) {
        //获取输入的名字
        var titleStr = dojo.byId('nameText').value;
        //获取当前所画的图形
        var cgraphic = map.graphics.graphics[index];
        //设置图形的属性，id、title
        cgraphic.attributes = { id: index, title: titleStr };
        tempGraphic = cgraphic;
        //对面图形进行geometryService的simplify操作
        geometryService.simplify([cgraphic], getLabelPoints);
        //获取当前所画图形的json字符串用来保存
        var graphicStr = dojo.toJson(cgraphic.toJson());
        //设置ajax请求的参数
        var params = { graphic: graphicStr }
        //用dojo的xhrGet的ajax方法把图形的json字符串提交到服务端保存
        dojo.xhrGet({ url: "saveG.aspx", handleAs: "text", preventCache: true, content: params, load: dojo.hitch(this, "saveEnd") });
        $.ajax({
        url：{% url 'save_graphic_url' %},
        type: "POST",
        data: params
        });
        //隐藏infoWindow
        map.infoWindow.hide();
    }

    function addToMap(evt) {
        var symbol;
        toolbar.deactivate();
        map.showZoomSlider();
        symbol = new SimpleFillSymbol();
        var graphic = new Graphic(evt.geometry, symbol);
        map.graphics.add(graphic);
        

        var centerPoint = map.toScreen(graphic.geometry.getExtent().getCenter());
        map.infoWindow.show(centerPoint);
        var index = map.graphics.graphics.length - 1;
        //设置infoWindow的显示内容
        var content = "<div>名称：</div><div><input type='text' id='nameText' name='nameText' /></div><div><input id ='savegraphic'type='button' name='Submit' value='保 存'  />&nbsp;&nbsp;&nbsp;&nbsp;<input type='button' name='Submit' value='取 消' onclick=cancel('" + index + "') /></div>";
        map.infoWindow.setContent(content);
        var al = document.getElementById("savegraphic");
        al.onclick = function (e) {
            savegraphic(1);
        }
    }

    
});

