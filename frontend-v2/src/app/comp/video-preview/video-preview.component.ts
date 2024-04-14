import { Component, OnInit } from '@angular/core';
import { VideoService } from '../../services/video.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-video-preview',
  templateUrl: './video-preview.component.html',
  styleUrl: './video-preview.component.css'
})
export class VideoPreviewComponent implements OnInit {

  public video_id!: string;
  public video_url!: string;
  public is_active!: boolean;

  constructor(private _videoService: VideoService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    let id =  this.route.snapshot.paramMap.get('feed_id');
    this.video_id = id ?? '';
    this._videoService.getVideo(id ?? '' ).subscribe(
      data => {
        this.is_active = data.is_active;
        this.video_url = this._videoService._videoURL + "/" + id;
      },
      error => {
        console.log(error);
      }
    );
  }
  

}
