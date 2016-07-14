from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[3.115667,3.908806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LAMOST_J001227.76+035431.7/sdB_LAMOST_J001227.76+035431.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LAMOST_J001227.76+035431.7/sdB_LAMOST_J001227.76+035431.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
