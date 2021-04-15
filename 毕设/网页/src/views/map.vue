<template>
  <div id="baiduMap"></div>
</template>

<script>
	export default {
		name: 'map',
		activated() {
			this.initBaiduMap();
		},
		data () {
			return {
			CityInfo: {
				longitude: 104.06, 
				latitude: 30.67
				},
			}
		},
		methods: {
			initBaiduMap() {
				var map = new BMap.Map('baiduMap');
				var c = new BMap.Point(116.404, 39.915);
				var _self = this;
				map.centerAndZoom(c, 15);
				var busline = new BMap.BusLineSearch('北京市',{
					renderOptions:{map:map,panel:"r-result"},
					onGetBusListComplete: function(result){
						if(result) {
							var fstLine = result.getBusListItem(0);//获取第一个公交列表显示到map上
							busline.getBusLine(fstLine);
						}
					}
				});
				function busSearch(){
					var busName = _self.$store.state.route;
					busline.getBusList(busName);
				}
				busSearch();
				map.enableScrollWheelZoom(true);
			}
		},
	}
</script>

<style>
    body,
    html,
    #baiduMap {
        overflow: hidden;
        width: 100%;
        height: 100%;
        margin: 0;
        font-family: "微软雅黑";
    }
    .info {
        z-index: 999;
        width: auto;
        min-width: 22rem;
        padding: .75rem 1.25rem;
        margin-left: 1.25rem;
        position: fixed;
        top: 1rem;
        background-color: #fff;
        border-radius: .25rem;
        font-size: 14px;
        color: #666;
        box-shadow: 0 2px 6px 0 rgba(27, 142, 236, 0.5);
    }
</style>