from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.35825,27.080111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_165325.98+270448.4/sdB_SDSSJ910_165325.98+270448.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_165325.98+270448.4/sdB_SDSSJ910_165325.98+270448.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
