from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[335.746167,51.689392],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_2220+5126/sdB_KPD_2220+5126_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_2220+5126/sdB_KPD_2220+5126_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
