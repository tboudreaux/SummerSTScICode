from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[256.689875,24.535722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_170645.57+243208.6/sdB_SDSSJ_170645.57+243208.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_170645.57+243208.6/sdB_SDSSJ_170645.57+243208.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
