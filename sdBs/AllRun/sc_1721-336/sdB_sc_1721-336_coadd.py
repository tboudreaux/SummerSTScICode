from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[261.144958,-33.684719],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sc_1721-336/sdB_sc_1721-336_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sc_1721-336/sdB_sc_1721-336_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
