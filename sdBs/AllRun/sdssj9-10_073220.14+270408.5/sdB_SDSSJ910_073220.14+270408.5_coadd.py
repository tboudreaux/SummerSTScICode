from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[113.083917,27.069028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_073220.14+270408.5/sdB_SDSSJ910_073220.14+270408.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_073220.14+270408.5/sdB_SDSSJ910_073220.14+270408.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
