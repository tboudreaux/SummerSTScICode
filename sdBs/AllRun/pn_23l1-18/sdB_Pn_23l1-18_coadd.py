from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[351.718417,12.506181],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Pn_23l1-18/sdB_Pn_23l1-18_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Pn_23l1-18/sdB_Pn_23l1-18_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
