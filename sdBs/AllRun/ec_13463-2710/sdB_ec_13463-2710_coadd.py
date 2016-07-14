from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[207.298292,-27.425128],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_13463-2710/sdB_ec_13463-2710_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_13463-2710/sdB_ec_13463-2710_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
