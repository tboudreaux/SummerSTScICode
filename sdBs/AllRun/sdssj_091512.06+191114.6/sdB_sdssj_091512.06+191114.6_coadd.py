from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[138.80025,19.187389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_091512.06+191114.6/sdB_sdssj_091512.06+191114.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_091512.06+191114.6/sdB_sdssj_091512.06+191114.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
