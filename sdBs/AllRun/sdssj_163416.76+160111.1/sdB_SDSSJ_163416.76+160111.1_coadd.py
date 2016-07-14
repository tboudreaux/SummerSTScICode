from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.569833,16.01975],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_163416.76+160111.1/sdB_SDSSJ_163416.76+160111.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_163416.76+160111.1/sdB_SDSSJ_163416.76+160111.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
