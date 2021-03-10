<template>
	<v-app>
		<v-main>
			<v-card	>
				<v-card-title style="background-color: #6BAAFE;">
					<font color="white">路线变更详情</font>
				</v-card-title>
				<v-container>
					<v-timeline
					    align-top
					    :dense="$vuetify.breakpoint.smAndDown"
					  >
					    <v-timeline-item
					      color="#6BAAFE"
					      v-for="(item, i) in detailData"
					      :key="i"
					      fill-dot
						  small
					    >
							<span slot="opposite">{{item.adjustTime + " / " + item.infoTime}}</span>
							<v-card color="#6BAAFE" dark>
								<v-card-title>
									{{item.content}}
								</v-card-title>
								<v-card-text class="white text--primary">
								  <p>{{item.route}}</p>
								  <v-btn
									color="#6BAAFE"
									class="mx-0"
									outlined
								  >
									查看路线图
								  </v-btn>
								</v-card-text>
							</v-card>
					    </v-timeline-item>
					</v-timeline>
				</v-container>
			</v-card>
		</v-main>
	</v-app>
</template>

<script>
  export default {
    name: 'detail',
	watch:{
	},
    data(){
		return {
			detailData:[
				{
					adjustTime:'2021.01.10',
					infoTime:'2021.01.05',
					content:'新增一号站点',
					route:'一号站点-二号站点'
				}
			]
		}
	}
  }

</script>

<style>
</style>
