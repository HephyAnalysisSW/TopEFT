
#include "TColor.h"
#include "TStyle.h"

void niceColorPalette( Int_t NCont = 255 ) {
 const Int_t NRGBs = 5;
 Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
 Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
 Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
 Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
 TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
 gStyle->SetNumberContours(NCont);
}

//void redColorPalette( Int_t NCont = 255 ) {
// const Int_t NRGBs = 3;
// Double_t stops[NRGBs] = { 0.00, 0.60, 1.00 };
// Double_t red[NRGBs]   = { 1.00, 0.70, 0.90 };
// Double_t green[NRGBs] = { 1.00, 0.70, 0.70 };
// Double_t blue[NRGBs]  = { 1.00, 0.90, 0.70 };
// TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
// gStyle->SetNumberContours(NCont);
//}


void redColorPalette( Int_t NCont = 255 ) {
 const Int_t NRGBs = 3;
 Double_t stops[NRGBs] = { 0.00, 0.60, 1.00 };
 Double_t red[NRGBs]   = { 1.00, 0.80*38/255,  0.70*246/255 };
 Double_t green[NRGBs] = { 1.00, 0.80*119/255, 0.70*121/255 };
 Double_t blue[NRGBs]  = { 1.00, 0.80*187/255, 0.70*68/255 };
 TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
 gStyle->SetNumberContours(NCont);
}


