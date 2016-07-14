from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[43.377917,-71.375492],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CPD-71_172/sdB_CPD-71_172_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CPD-71_172/sdB_CPD-71_172_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
