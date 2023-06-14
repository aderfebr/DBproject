<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script setup>
import axios from 'axios';
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from 'echarts/components';
import VChart, { THEME_KEY } from 'vue-echarts';
import { ref, provide } from 'vue';

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

const option = ref({
  title: {
    text: '',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  series: [
    {
      type: 'pie',
      radius: '50%',
      data: [
        { value: 0, name: '总人流量' },
        { value: 0, name: '在镜人流量' },
        { value: 0, name: '入口人流量' },
        { value: 0, name: '出口人流量' },
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
});

const props = defineProps({
        num:Number
});

axios.get('http://localhost:8000/api/crowdvis/')
  .then(res => {
    option.value.series[0].data[0].value=res.data[props.num].total_count;
    option.value.series[0].data[1].value=res.data[props.num].vis_count;
    option.value.series[0].data[2].value=res.data[props.num].in_count;
    option.value.series[0].data[3].value=res.data[props.num].out_count;
    option.value.title.text="设备编号："+res.data[props.num].device_id_id;
  });

</script>