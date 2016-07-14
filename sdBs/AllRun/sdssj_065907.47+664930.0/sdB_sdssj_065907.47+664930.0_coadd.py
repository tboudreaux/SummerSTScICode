from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[104.781125,66.825],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_065907.47+664930.0/sdB_sdssj_065907.47+664930.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_065907.47+664930.0/sdB_sdssj_065907.47+664930.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
