from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.042167,-1.976694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_135210.12-015836.1/sdB_SDSSJ_135210.12-015836.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_135210.12-015836.1/sdB_SDSSJ_135210.12-015836.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
