<template>
	<v-app
	id = 'homepage'>
		<v-main>
			<v-card>
				<v-toolbar
				  color="#6BAAFE"
				  dark
				  flat>
				<v-toolbar-title style="font-size: 28px;">北京公交乘车公告</v-toolbar-title>
				
				<v-spacer></v-spacer>
				<v-btn text @click="updateBusRoute"><font color="white" size="4">更新公交路线</font></v-btn>
				<v-btn text @click="updateNews"><font color="white" size="4">更新乘车公告</font></v-btn>
				<template v-slot:extension>
				<v-tabs 
					background-color='#6BAAFE'
					centered
					fixed-tabs
				>
					<v-tabs-slider color="yellow"></v-tabs-slider>
					<v-tab color="#6BAAFE" flat><font color="white" size="4">乘车公告</font></v-tab>
					<v-tab color="#6BAAFE" flat><font color="white" size="4">更新日志</font></v-tab>
					<v-card flat width="300" color="#ffffff">
					    <v-select
					        :items="busRouters"
					        v-model="selectBus"
							background-color="#6BAAFE"
					        solo
					        flat
					        style="text-align: center;font-size: 18px;-webkit-text-fill-color:white;"
					    >
					    </v-select>
					</v-card>
					<v-card flat width="300" color="#ffffff">
						<v-select
						    :items="reason"
						    v-model="selectReason"
							background-color="#6BAAFE"
						    solo
						    flat
						    style="text-align: center;font-size: 18px;-webkit-text-fill-color:white;text-emphasis-style: initial;"
						>
						</v-select>
					</v-card>
					<v-tab-item>
						<v-row
							justify="left"
						>
							<v-col md="2">
								<v-treeview
									activatable
									multiple-active=false
									color="#6ABBFE"
									:items="timeSelector">
								</v-treeview>
							</v-col>
							<v-divider vertical></v-divider>
							<v-col>
								<v-card 
									flat
								>
										<v-data-table
											:headers = "headers"
											:items = "notices"
											:rows-per-page-items="1"
											height="630px"
											>
										</v-data-table>
								</v-card>
							</v-col>
						</v-row>
					</v-tab-item>
					<v-tab-item>
						<v-container style="margin: -webkit-calc();">
							<v-data-table
								:headers="logHeaders"
								:items="logDetails"
							>
							</v-data-table>
						</v-container>
					</v-tab-item>
				</v-tabs>
				</template>
				</v-toolbar>
			</v-card>
		</v-main>
	</v-app>
</template>

<script>
  export default {
    name: 'HomePage',
	watch:{
		selectBus(){
			if(this.selectBus == '所有路线'){
				return;
			}
			else{
				var _self = this;
				this.$store.commit('setRoute',{route:_self.selectBus});
				this.$router.push('/detail');
			}
		}
	},
	beforeCreate() {
		var date = new Date();
		var year = date.getFullYear();
		var month = date.getMonth();
		var timeSelector = [];
		var months = ['1月/January','2月/February','3月/March','4月/April','5月/May','6月/June','7月/July','8月/August','9月/September','10月/October','11月/November','12月/December'];
		var curChild = [];
		var id = 2;
		while (id-2 <= month){
			curChild.push({'id':id,'name':months[id-2]});
			id ++;
		}
		var curYear = {
			id:1,
			name:year,
			children:curChild
		};
		timeSelector.push(curYear);
		var yearCnt = year-1;
		while(yearCnt >= 2010){
			curChild = [];
			var monthCnt = 1;
			var yearId = id;
			id ++;
			while(monthCnt <= 12){
				curChild.push({'id':id,'name':months[monthCnt-1]});
				id ++;
				monthCnt ++;
			}
			curYear = {
				id:yearId,
				name:yearCnt,
				children:curChild
			};
			timeSelector.push(curYear);
			yearCnt --;
		}
		this.$store.commit('setTimeSelector',{'timeSelector':timeSelector});
	},
    mounted() {
		var _self = this;
    	this.$axios.get(
						"/api/"
						).then(
							function(response){
							 var data = response.data.ret;
							 data = JSON.parse(data);
							 _self.notices = data;
						}).catch(function(err){
							alert(err);
						}); 

    },
	data(){
		var _self = this;
		return	{
			search:'',
			selectBus:'所有路线',
			selectReason:'变更缘由',
			busRouters:_self.$store.state.busRoutes.split(' '),
			reason:[
				'变更缘由',
				'征集活动',
				'公交新策',
				'节假日',
				'大型活动',
				'高铁线路规划',
				'地铁线路规划',
				'站线规范撤销',
				'配合路况调整',
				'天气影响',
				'政府部门调整要求',
				'优化调整',
				'调整营业时间'
			],
			headers:[
				{text:'发布时间',align:'center',value:'time',width:125},
				{text:'标题',value:'title',align:'center',width:200},
				{text:'分类',value:'classification',align:'center',width:100},
				{text:'修改路线、站点及方法',align:'center',filterable: false,value:'content'}
			],
			notices:[
				{
					time:'2021.01.12',
					title:'标题',
					classification:'天气',
					content:'一号线:\n\t一号站点：取消\n\t二号站点：新增'
				}
			],
			logHeaders:[
				{text:'操作时间',value:'operateTime'},
				{text:'更新时间段',value:'updateTime'},
				{text:'更新数量',value:'updateNum'}
			],
			logDetails:[
				{
					operateTime:'2021.01.12',
					updateTime:'2021.01.01-2021.01.12',
					updateNum:'2',
				},
				{
					operateTime:'2021.01.01',
					updateTime:'2020.12.13-2021.01.01',
					updateNum:'4',
				}
			],
			timeSelector : _self.$store.state.timeSelector,
		}
	},
    methods:{
		updateBusRoute(){
			alert("1");
		},
		updateNews(){
			alert("2");
		},
	}
  }
</script>
<style>
	.v-data-table tr {
	  height: 50px;
	  overflow-y: hidden;
	}
</style>