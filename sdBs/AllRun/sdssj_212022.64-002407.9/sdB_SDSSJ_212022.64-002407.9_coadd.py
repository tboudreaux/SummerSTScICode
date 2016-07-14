from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[320.094333,0.402194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_212022.64-002407.9/sdB_SDSSJ_212022.64-002407.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_212022.64-002407.9/sdB_SDSSJ_212022.64-002407.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
