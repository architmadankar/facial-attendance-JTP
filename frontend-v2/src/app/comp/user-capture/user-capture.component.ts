import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-user-capture',
  templateUrl: './user-capture.component.html',
  styleUrl: './user-capture.component.css'
})
export class UserCaptureComponent implements OnInit {

  @ViewChild("video")
  public video: ElementRef = {} as ElementRef;
  
  @ViewChild("canvas")
  public canvas: ElementRef = {} as ElementRef;

  errMsg = '';
  public captures: Array<any>;
  public bCapture: Array<Blob>;
  public user_id: string = '';

  constructor(private _userService: UserService, private route: ActivatedRoute, private _router: Router) {
    this.captures = [];
    this.bCapture = [];
  }

  ngOnInit(): void {
    let id = this.route.snapshot.paramMap.get('user_id');
    this.user_id = id!;
  }

  ngAfterViewInit() {
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ audio: false, video: true }).then(stream => {
        this.video.nativeElement.srcObject = stream;
        this.video.nativeElement.play();
      });
    }
  }

  public capture() {
    this.canvas.nativeElement.getContext("2d").drawImage(this.video.nativeElement, 0, 0, 640, 480);
    this.captures.push(this.canvas.nativeElement.toDataURL("image/jpg"));
    this.canvas.nativeElement.toBlob((blob: Blob) => {
      this.bCapture.push(blob);
    }, 'image/jpg', 0.95);
  }

  public resetCamera() {
    this.captures = [];
    this.bCapture = [] as Blob[];
  }

  public saveCapture() {
    console.log(this.captures.length);
    if (this.bCapture.length < 5) {
      this.errMsg = "Please capture 5 images";
    } else {
      for(var i = 0; i < this.bCapture.length; i++) {
        console.log(this.bCapture[i]);
        const formData = new FormData();
        const file = new File([this.bCapture[i]], 'sed.jpg', { type: 'image/jpg' });
        formData.append('image', file);
        this._userService.captureUser(this.user_id, formData).subscribe({
          next: data => console.log(data),
          error: error => console.log(error)
        });
    }
    this.resetCamera();
    this._router.navigate(['../../'], { relativeTo: this.route});
    this._userService.trainClassifier().subscribe({
      next: data => console.log(data),
      error: error => console.log(error)
    });
  }
}
}