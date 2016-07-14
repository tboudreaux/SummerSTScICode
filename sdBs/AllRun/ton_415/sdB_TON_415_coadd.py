from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[141.305333,31.810528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_TON_415/sdB_TON_415_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_TON_415/sdB_TON_415_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
