import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { IVideo } from '../../interface/ivideo';
import { Router, ActivatedRoute } from '@angular/router';
import { VideoService } from '../../services/video.service';
import { faTrashAlt, faVideo, faCircle, faStop, faPlay } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-video-list',
  templateUrl: './video-list.component.html',
  styleUrl: './video-list.component.css'
})
export class VideoListComponent implements OnInit {

  videoFeedForm!: FormGroup;
  
  public formIsCollapsed = true;
  public videos: IVideo[] = [];

  videoIcon = faVideo;
  trashIcon = faTrashAlt;
  circleIcon = faCircle;
  stopIcon = faStop;
  playIcon = faPlay;

  addRespMsg: string = '';
  deleteRespMsg: string = '';

  constructor (private _videoService: VideoService, private fb: FormBuilder, private _router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.videoFeedForm = this.fb.group({
      id: ['', Validators.required],
      url: ['', Validators.required]
    })
    this._videoService.getVideoList().subscribe(
      data => {
        this.videos = data;
      },
      error => {
        console.log(error);
      }
    );
      
  }

  get id(){
    return this.videoFeedForm.get('id');
  }
  get url(){
    return this.videoFeedForm.get('url');
  }

  addVideo(){
    console.log(this.videoFeedForm.value);
    this._videoService.addVideo(this.videoFeedForm.value).subscribe(
      data => {
        this.videos.push(data);
        this.deleteRespMsg = '';
        this.addRespMsg = 'Video added successfully';
      });
  }

  deleteVideo(video_id: any, index: number){
    this._videoService.deleteVideo(video_id).subscribe(
      data => {
        this.addRespMsg = ''; 
        this.deleteRespMsg = data.message;
        this.videos.splice(index, 1); 
      
    },
    error => {
      console.log(error);
    }
  );
  }
  toggleVideo(video_id: any){
    let is_active: Boolean;
    for ( var video of this.videos){
      if (video.id == video_id){
        is_active = video.is_active;
        if (is_active == true){
          this._videoService.stop_video(video_id).subscribe(
            data => console.log(data),
            error => console.log(error)
          );
          return video.is_active = false;
        } else{
          this._videoService.startVideo(video_id).subscribe(
            data => console.log(data),
            error => console.log(error)
          );
          this._router.navigate(['/video/' + video_id], {relativeTo: this.route});
          return video.is_active = true;
        }
      }
    }
    return false;
  }
  videoPreview(video_id: string){
    return "/video/" + video_id.toString();
  }
}
