from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.870958,16.75275],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_125129.03+164509.9/sdB_SDSSJ910_125129.03+164509.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_125129.03+164509.9/sdB_SDSSJ910_125129.03+164509.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
