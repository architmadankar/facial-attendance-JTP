import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserCaptureComponent } from './user-capture.component';

describe('UserCaptureComponent', () => {
  let component: UserCaptureComponent;
  let fixture: ComponentFixture<UserCaptureComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [UserCaptureComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(UserCaptureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
