from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[256.818875,27.902889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_170716.53+275410.4/sdB_SDSSJ_170716.53+275410.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_170716.53+275410.4/sdB_SDSSJ_170716.53+275410.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
