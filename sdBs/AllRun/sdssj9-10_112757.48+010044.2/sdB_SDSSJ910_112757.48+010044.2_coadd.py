from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[171.9895,1.012278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_112757.48+010044.2/sdB_SDSSJ910_112757.48+010044.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_112757.48+010044.2/sdB_SDSSJ910_112757.48+010044.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
