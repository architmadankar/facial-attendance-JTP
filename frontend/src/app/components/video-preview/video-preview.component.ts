import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { VideoService } from '../../services/video.service';

@Component({
  selector: 'app-video-preview',
  templateUrl: './video-preview.component.html',
  styleUrls: ['./video-preview.component.css']
})
export class VideoPreviewComponent implements OnInit {

  public feed_id!: string;
  public _feedUrl!: string;
  public is_active!: boolean;

  constructor(private _videoFeedService: VideoService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    let id = this.route.snapshot.paramMap.get('feed_id');
    this.feed_id = id!;
    this._videoFeedService.getVideoFeed(id!).subscribe(
      res => {
        console.log(res);
        this.is_active = res.is_active;

        this._feedUrl = this._videoFeedService._feedPreviewUrl + "/" + id;

      },

    );
  }

}
