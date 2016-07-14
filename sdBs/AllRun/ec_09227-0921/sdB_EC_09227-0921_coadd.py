from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[141.308875,-9.581619],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_09227-0921/sdB_EC_09227-0921_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_09227-0921/sdB_EC_09227-0921_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()