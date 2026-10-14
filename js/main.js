(function(){
  document.querySelectorAll('.yt').forEach(function(b){
    b.addEventListener('click',function(){
      var id=b.getAttribute('data-id');
      var f=document.createElement('iframe');
      f.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0';
      f.allow='accelerometer;autoplay;encrypted-media;gyroscope;picture-in-picture';
      f.allowFullscreen=true;f.title=b.getAttribute('aria-label')||'Vídeo';
      b.innerHTML='';b.appendChild(f);b.style.cursor='default';
    },{once:true});
  });
})();
