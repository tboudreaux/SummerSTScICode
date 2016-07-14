from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[245.148875,7.786639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_162035.73+074711.9/sdB_sdssj_162035.73+074711.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_162035.73+074711.9/sdB_sdssj_162035.73+074711.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
