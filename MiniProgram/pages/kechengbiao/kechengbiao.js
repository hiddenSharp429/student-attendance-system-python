var colors = require('../../utils/colors')
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    weekArray: ['第1周', '第2周', '第3周', '第4周', '第5周', '第6周', '第7周', '第8周', '第9周', '第10周', '第11周', '第12周', '第13周', '第14周', '第15周', '第16周', '第17周', '第18周', '第19周', '第20周'],
    pageNum: 0, // 当前所在分类的索引
    todayDay: '', // 今日日期
    todayMonth:'', // 今日月份
    todayWeek:'', // 今日周
    day:'', // 日期
    month: '', // 月份
    monthNum:1,
    week: ['日','一', '二', '三', '四', '五', '六'], // 周日为起始日
    nowDay:[1,2,3,4,5,6,7], // 本周的七天日期
    schoolTime: ['2022','09','04'], // 本学期开学时间
    nowWeek: '', // 当前周
    course_time:[
      ['8:00','8:45'],
      ['8:55','9:40'],
      ['10:00','10:45'],
      ['10:55','11:40'],
      ['11:50','12:35'],
      ['14:00','14:45'],
      ['14:55','15:40'],
      ['16:00','16:45'],
      ['16:55','17:40'],
      ['17:50','18:35'],
      ['19:20','20:05'],
      ['20:15','21:00'],
      ['21:10','21:55'],
  ],

  wList: [
    [     //第一周 
      // { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
      { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
      { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },

      { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
      { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
      {"id":7,"isToday": 2, "jie": 7, "classNumber": 2, "name": "数学建模","address":"1215"},
     
      { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
      { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },

      { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
      { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
      
      { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
 ],
    [      //第二

      { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
      { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },

      { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
      { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
      {"id":7,"isToday": 2, "jie": 7, "classNumber": 2, "name": "数学建模","address":"未知"},
      { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
      { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },

      { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
      { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
      
      { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
      [     //第三周 
        { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
        { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
        { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },

        { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
        { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
        {"id":7,"isToday": 2, "jie": 7, "classNumber": 2, "name": "数学建模","address":"未知"},
        { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
        { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },

        { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
        { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
        
        { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
   ],
      [      //第四
  
        { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
        { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
        {"id":7,"isToday": 2, "jie": 7, "classNumber": 2, "name": "数学建模","address":"未知"},
        { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
        { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
       
        { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
        { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },

        { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
        { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
        
        { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
        [     //第5周 
          { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
          {"id":7,"isToday": 3, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
          { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
          { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
  
          { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
          { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
         
          { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
          { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
  
          { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
          { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
          
          { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
     ],
        [      //第6
    
          { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
          { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
          {"id":7,"isToday": 3, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
          { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
          { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
         
          { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
          { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
  
          { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
          { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
          
          { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
          [     //第7周 
            { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
            { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
            { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
            {"id":7,"isToday": 3, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
            { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
            { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
           
            { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
            { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
    
            { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
            { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
            
            { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
       ],
          [      //第8
      
            { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
            { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
            {"id":7,"isToday": 3, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
            { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
            { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
           
            { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
            { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
    
            { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
            { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
            
            { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
            [     //第9周 
              { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
              { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
              { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
              {"id":7,"isToday": 5, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
              { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
              { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
             
              { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
              { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
      
              { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
              { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
              
              { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
         ],
            [      //第10
        
              { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
              { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
              {"id":7,"isToday": 5, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
              { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
              { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
             
              { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
              { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
      
              { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
              { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
              
              { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
              [     //第11周 
                { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
                { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                {"id":7,"isToday": 5, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
                { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
               
                { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
        
                { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
                
                { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
           ],
              [      //第12
          
                { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                {"id":7,"isToday": 5, "jie": 1, "classNumber": 2, "name": "数学建模","address":"未知"},
                { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
               
                { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
        
                { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
                
                { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
                [     //第13周 
                  { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
                  { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                  { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                  {"id":7,"isToday": 3, "jie": 5, "classNumber": 2, "name": "数学建模","address":"未知"},
                  { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                  { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
                 
                  { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                  { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
          
                  { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                  { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
                  
                  { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
             ],
                [      //第14
            
                  { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                  { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                  {"id":7,"isToday": 3, "jie": 5, "classNumber": 2, "name": "数学建模","address":"未知"},
                  { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                  { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
                 
                  { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                  { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
          
                  { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                  { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
                  
                  { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
                  [     //第15周 
                    { "id":1,"isToday": 1, "jie": 7, "classNumber": 2, "name": "算法设计与分析","address":"2306" },
                    { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                    { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                    {"id":7,"isToday": 3, "jie": 5, "classNumber": 2, "name": "数学建模","address":"未知"},
                    { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                    { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
                   
                    { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                    { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
            
                    { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                    { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "计算机网络" ,"address":"2304" },
                    
                    { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },
               ],
                  [      //第16
              
                    { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                    { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                    {"id":7,"isToday": 3, "jie": 5, "classNumber": 2, "name": "数学建模","address":"未知"},
                    { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                    { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
                   
                    { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                    { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
            
                    { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                    { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
                    
                    { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
                    [      //第17
              
                      { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                      { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                      {"id":7,"isToday": 3, "jie": 5, "classNumber": 2, "name": "数学建模","address":"未知"},
                      { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                      { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
                     
                      { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                      { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
              
                      { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                      { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
                      
                      { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },],
                      [      //第18
              
                        { "id":2,"isToday": 1, "jie": 1, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                        { "id":3,"isToday": 1, "jie": 3, "classNumber": 2, "name": "毛概","address":"6202" },
                        {"id":7,"isToday": 3, "jie": 5, "classNumber": 2, "name": "数学建模","address":"未知"},
                        { "id":4,"isToday": 2, "jie": 3, "classNumber": 2, "name": "Matlab" ,"address":"2306" },
                        { "id":5,"isToday": 2, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"1104" },
                       
                        { "id":6,"isToday": 3, "jie": 3, "classNumber": 2, "name": "计算机网络" ,"address":"5102" },
                        { "id":2,"isToday": 3, "jie": 7, "classNumber": 2, "name": "操作系统" ,"address":"5409" },
                
                        { "id":3,"isToday": 4, "jie": 1, "classNumber": 2, "name": "毛概" ,"address":"6202" },
                        { "id":6,"isToday": 4, "jie": 5, "classNumber": 2, "name": "数据库原理及应用" ,"address":"2306" },
                        
                        { "id":1,"isToday": 5, "jie": 3, "classNumber": 2, "name": "算法设计与分析" ,"address":"5506" },]
]
  },



  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    app.editTabBar();    //显示自定义的底部导航

    let nowWeek = this.getNowWeek()
    let nowDay = this.getDayOfWeek(nowWeek)
    let pageNum = nowWeek - 1
    let month = this.getMonth((nowWeek - 1) * 7);
    // this.data.todayMonth
    this.setData({
      todayMonth: new Date().getMonth() + 1,
      day: new Date().getDate(),
      month: new Date().getMonth() + 1,
      todayDay: new Date().getDate(),
      nowWeek,
      nowDay: this.getDayOfWeek(nowWeek),
      pageNum,
      // todayWeek:nowWeek,
      monthNum: month / 1, // 当前月份数字类型，用于数字运算
      colorArrays: colors, // 课表颜色
      schoolTime: [2023, 9, 4], // 确保其他方法使用更新后的日期
    })

// // 获取数据库信息
// var apiUrl = 'http://43.136.80.11:5000/student_manager/view_student_courses'
// var that = this;

// wx.request({
//   url: apiUrl,
//   method: 'GET',
//   header: {
//     'app': 'wx-app'
//   },
//   data: {
//     // 需要传入的参数
//         'student_id':'2021611001',
//         'semester': '2023',
//         'week_no': 5
//   },
//   success: function (res) {
//     if (res.statusCode === 200) {
//       // 接受参数
//       var result = res.data;
//       const wList = result.class_schedule_records
//       console.log(wList)

//       that.setData({
//         wList: wList
//       })
//     }
//     else {
//       // 捕捉状态报错
//       console.error('Error:', res.statusCode, res.data);
//     }
//   },
  
//   fail: function (error) {
//     // 捕捉请求报错
//     console.error('Request failed:', error);
//   }
 
// })

  },

  // 获取第几周后的月份
  getMonth(days) {
    let [year,month,day] = this.data.schoolTime
    var date = new Date(year,month-1,day);    
    date.setDate(date.getDate() + days);//获取n天后的日期      
    var m = (date.getMonth() + 1) < 10 ? "0" + (date.getMonth() + 1) : (date.getMonth() + 1);        
    return  m;     
  },

  // 获取第几周后的星期几的日期
  getDay(days) {
    let [year, month, day] = this.data.schoolTime
    var date = new Date(year, month-1, day);
    date.setDate(date.getDate() + days);//获取n天后的日期      
    var d = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();//获取当前几号，不足10补0    
    return d;
  },

  // 获取当前周
  getNowWeek(){
    var date = new Date();
    let [year, month, day] = this.data.schoolTime
    var start = new Date(year, month-1, day);
    //计算时间差
    var left_time = parseInt((date.getTime()-start.getTime())/1000)+24 * 60 * 60;
    var days = parseInt(left_time/3600/24);
    var week = Math.floor(days / 7) + 1;
    var result = week
    if(week>20 || week <= 0){
      result = this.data.now_week;
    }
    return result
  },

  // 判断是否是月份的第一天
  isFirstDayOfMonth(date) {
    return date.getDate() === 1;
  },

  //获取一周的日期
  getDayOfWeek(week){
    var day = []
    for (var i = -1; i < 6; i++) {
      var days = (week - 1) * 7 + i;
      let currentDate = this.getDateAfterDays(days);
      day.push({
        day: this.getDay(days),
        isMonthStart: this.isFirstDayOfMonth(currentDate),
        month: currentDate.getMonth() + 1
      })
    }
    return day
  },
  // 获取n天后的日期
  getDateAfterDays(days) {
    let [year, month, day] = this.data.schoolTime;
    var date = new Date(year, month-1, day);
    date.setDate(date.getDate() + days);
    return date;
  },

  // 获取课表数据
  async getCourseList(){

  },

  // 点击切换导航的回调
  changeNav(event){
    let pageNum = event.currentTarget.dataset.page
    let nowWeek = pageNum + 1
    let nowDay = this.getDayOfWeek(nowWeek)
    let month = this.getMonth((nowWeek-1)*7)
    this.setData({
      pageNum,
      nowWeek,
      nowDay,
      month,
      monthNum: month / 1, // 当前月份数字类型，用于数字运算
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    this.setData({
      todayDay: new Date().getDate(),
      todayMonth: new Date().getMonth() + 1,
      day: new Date().getDate(),
      month: new Date().getMonth() + 1,
    })
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})