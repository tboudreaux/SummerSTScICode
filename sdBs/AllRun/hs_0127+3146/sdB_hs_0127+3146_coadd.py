from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[22.469292,32.036117],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0127+3146/sdB_hs_0127+3146_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0127+3146/sdB_hs_0127+3146_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
