from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[288.844792,-50.321589],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22947-115/sdB_bps_cs22947-115_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22947-115/sdB_bps_cs22947-115_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
