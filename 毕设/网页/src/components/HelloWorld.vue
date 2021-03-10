<template>
	<v-app
	id = 'homepage'>
		<v-main>
			<v-card>
				<v-card-title >
					北京公交乘车公告
				</v-card-title>
				
				<v-tabs 
					background-color='#6BAAFE'
				>
					<v-tab><font color="white">乘车公告</font></v-tab>
					<v-tab><font color="white">更新日志</font></v-tab>
					<v-card flat width="137" color="#ffffff">
					    <v-select
					        :items="busRouters"
					        v-model="selectBus"
							background-color="#6BAAFE"
					        solo
					        flat
					        style="font-size: 14px;-webkit-text-fill-color:white;"
					    >
					    </v-select>
					</v-card>
					<v-tab-item>
						<v-row
							justify="left"
						>
							<v-col md="2">
								<v-treeview
									dense
									activatable
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
										:headers="headers"
										:items="notices"
										:search="search"
										style="white-space: pre-wrap;"
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
					<v-tab-item>
						
					</v-tab-item>
				</v-tabs>
			</v-card>
		</v-main>
	</v-app>
</template>

<script>
  export default {
    name: 'HelloWorld',
	watch:{
		selectBus(){
			if(this.selectBus == '所有路线'){
				
			}
			else{
				
			}
		}
	},
    data(){
		var _self = this;
		return	{
			search:'',
			selectBus:'所有路线',
			busRouters:[
				'所有路线',
				'一号线',
				'二号线',
				'三号线'
			],
			headers:[
				{text:'发布时间',align:'start',value:'time'},
				{text:'标题',value:'title'},
				{text:'调整时间',value:'adjustTime'},
				{text:'调整原因',value:'adjustReason'},
				{text:'修改路线、站点及方法',filterable: false,value:'adjustMethod'}
			],
			notices:[
				{
					time:'2021.01.12',
					title:'标题',
					adjustTime:'2021.01.16',
					adjustReason:'天气',
					adjustMethod:'一号线:\n\t一号站点：取消\n\t二号站点：新增'
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
			timeSelector : [
				{
					name:'2021',
					children:[
						{ name: '1月/January' },
						{ name: '2月/JFebruary' },
						{ name: '3月/March' },
						{ name: '4月/April' },
						{ name: '5月/May' },
						{ name: '6月/June' },
						{ name: '7月/July' },
						{ name: '8月/August' },
						{ name: '9月/September' },
						{ name: '10月/October' },
						{ name: '11月/November' },
						{ name: '12月/December' },
					]
				}	
			],
		}
	}
  }
</script>