from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[352.309917,51.315964],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_2326+5102/sdB_KPD_2326+5102_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_2326+5102/sdB_KPD_2326+5102_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
