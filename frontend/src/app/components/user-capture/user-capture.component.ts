import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../../services/user.service';


@Component({
  selector: 'app-user-capture',
  templateUrl: './user-capture.component.html',
  styleUrls: ['./user-capture.component.css']
})
export class UserCaptureComponent implements OnInit {

  @ViewChild("video")
  public video: ElementRef = {} as ElementRef;

  @ViewChild("canvas")
  public canvas: ElementRef = {} as ElementRef;

  errorMsg = "";
  public captures: Array<any>;
  public blobCaptures: Array<Blob>;
  public user_id: string = '';
  
  constructor(private _userService: UserService, private route: ActivatedRoute, private _router: Router) {
    this.captures = [];
    this.blobCaptures = [];
    }

  ngOnInit(): void {
    let id = this.route.snapshot.paramMap.get('user_id');
    this.user_id = id!;
  }

  public ngAfterViewInit() {
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true, audio: false }).then(stream => {
            this.video.nativeElement.srcObject = stream;
            this.video.nativeElement.play();
        });
    }
  }
  
  public capture() {
    var context = this.canvas.nativeElement.getContext("2d").drawImage(this.video.nativeElement, 0, 0, 640, 480);
    this.captures.push(this.canvas.nativeElement.toDataURL("image/jpg"));
    this.canvas.nativeElement.toBlob((blob: Blob) => {
      this.blobCaptures.push(blob);
    }, "image/jpg", 0.95);
  }

  public resetCaptures(){
    this.captures = [];
    this.blobCaptures = [] as Blob[];
  }

  public saveCaptures(){
    console.log(this.captures.length);
    if (this.captures.length < 5){
      this.errorMsg = "Minimum 5 face captures are required.";
    }else{
      for(var i = 0; i < this.blobCaptures.length; i++){
        console.log(this.blobCaptures[i]);
        const formData = new FormData();
        const file = new File([this.blobCaptures[i]], 'name.jpg', {type:'image/jpg'});
        formData.append('image', file);
        this._userService.captureUser(this.user_id, formData).subscribe(
          res => console.log(res),
          err => console.log(err)
        );
      }
      this.resetCaptures();
      this._router.navigate(['../../'], {relativeTo: this.route});
      this._userService.trainClassifier().subscribe(
        res => console.log(res),
        err => console.log(err)
      );
    }
  }

}
